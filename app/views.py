from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from random import randint
from reportlab.lib import colors
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from app.forms import FormFillForm
from app.models import FormFill


class FormFillView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = FormFillForm
    model = FormFill

    def form_valid(self, form):
        try:
            form.instance.user_name = self.request.user
            return super(FormFillView, self).form_valid(form)
        except IntegrityError:
            return HttpResponse('error')


class UserDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    template_name = 'app/userinfo_detail.html'
    queryset = User.objects.all()
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['formfill'] = FormFill.objects.all()
        return context


@login_required()
def login_page(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('home')


@login_required()
def pdf_generator(request):
    response = HttpResponse(content_type='application/pdf')
    filename = 'hall_ticket_' + str(request.user)
    response['content-Disposition'] = f'inline; filename="{filename}.pdf"'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    # Head title with address
    c.setFontSize(25)
    c.setFillColor(colors.orangered)
    c.drawCentredString(300, 800, 'State College Common Entrance Test')
    c.setFillColor(colors.black)
    c.setFontSize(14)
    c.drawCentredString(300, 760, 'Admit Card for SCCET - 2020')
    # line
    c.line(75, 750, 550, 750)
    # user info
    c.setFillColor(colors.gray)
    c.drawString(75, 730, 'Username:')
    c.drawString(75, 710, 'Name:')
    c.drawString(75, 690, 'Email')
    c.drawString(75, 670, 'Date Of Birth:')
    c.drawString(75, 650, 'Address:')

    c.setFillColor(colors.black)
    c.drawString(200, 730, f'{request.user.formfill.user_name}')
    c.drawString(200, 710, f'{request.user.formfill.first_name} {request.user.formfill.last_name}')
    c.drawString(200, 690, f'{request.user.formfill.email}')
    c.drawString(200, 670, f'{request.user.formfill.dob}')
    c.drawString(200, 650, f'{request.user.formfill.address}')

    # user pic in same line of user info
    img = ImageReader(request.user.formfill.profile_pic)
    c.drawImage(img, 450, 600, 120, 140)
    c.line(75, 590, 550, 590)
    # examination centre or  exam date
    c.setFillColor(colors.gray)
    c.drawString(75, 570, 'Exam centre:')
    c.drawString(75, 530, 'Date:')
    c.drawString(75, 510, 'Time:')

    c.setFillColor(colors.black)
    r = randint(0, 13)
    centre = {
        'college': ['M. G. College', 'B. N. College', 'Nawab College', 'G. M. College', 'Hindu College',
                    'Lalan Singh College', 'M. G. college', 'Abdul kalam College', 'Lohia College', 'Anugrah College',
                    'Manas College', 'L. S. College', 'M. G. College', 'S. N. College'
                    ],
        'address': ['Patna', 'Gaya', 'Muzaffarpur', 'Nawada', 'Patna', 'Patna', 'Gaya', 'Purnia', 'BhagalPur',
                    'Dharbhnaga', 'Patna', 'Samstipur', 'Jehanabad', 'Patna'

                    ]
    }
    c.drawString(200, 570, centre['college'][r])
    c.drawString(200, 550, centre['address'][r])
    t = randint(0, 1)
    time = ['10:00 to 12:00', '1:00 to 3:00']
    c.drawString(200, 530, '6th june 2020')
    c.drawString(200, 510, time[t])
    # guidelines
    c.setFontSize(18)
    c.drawCentredString(300, 450, 'Guidelines')
    c.line(75, 440, 550, 440)

    c.setTitle(filename)
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
