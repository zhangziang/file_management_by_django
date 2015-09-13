# encoding: utf-8

from django.views.generic import TemplateView
from apps.file.models import File
from apps.college.models import College
from apps.course.models import Course


class IndexView(TemplateView):
    one_page_item = 20
    template_name = 'index.html'

    def get(self, request, page='1'):
        page = int(page)
        files = File.objects.all().order_by('-add_time')
        files_num = len(files)
        print files_num
        before_page_num = (page-1)*self.one_page_item
        current_page_end = page*self.one_page_item
        if page-1 <= 0:
            before_page = False
        else:
            before_page = True
        if current_page_end >= files_num:
            after_page = False
        else:
            after_page = True

        if before_page_num >= files_num or before_page_num < 0:
            files = []
        elif current_page_end >= files_num:
            files = files[before_page_num:]
        else:
            files = files[before_page_num:current_page_end]
        context = {
            'files': files,
            'before_page': before_page,
            'after_page': after_page,
            'page_next': str(page+1),
            'page_last': str(page-1),
        }
        return self.render_to_response(context)


class CourseListView(TemplateView):
    template_name = 'courses.html'

    def get(self, request, *args, **kwargs):
        colleges = College.objects.all()
        context = {
            'colleges': colleges,
        }
        return self.render_to_response(context)


class CourseView(TemplateView):
    template_name = 'course.html'

    def get(self, request, id):
        id = int(id)
        context = dict()
        try:
            course = Course.objects.get(pk=id)
            files = course.file_set.all().order_by('-add_time')
            context['exist'] = True
            context['files'] = files
            context['course'] = course
        except Course.DoesNotExist:
            context['exist'] = False

        return self.render_to_response(context)
