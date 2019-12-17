from .models import College, Student
from service_objects.services import Service


class CreateCollegeService(Service):
    def process(self):
        coll = self.data
        post_data = coll.get("college_data")
        college_name = post_data.get('college_name')
        city = post_data.get('city')
        state = post_data.get('state')
        college_obj = College.objects.create(
            college_name=college_name,
            city=city,
            state=state
        )
        return college_obj


class GetCollegeService(Service):
    def process(self):
        clg = self.data
        pk = clg.get('pk')
        if pk:
            college_gt = College.objects.get(id=pk)
        else:
            college_gt = College.objects.all()
        return college_gt


class DeleteCollegeService(Service):
    def process(self):

        pk = self.data.get('pk')
        college_dlt = College.objects.get(pk=pk)
        college_dlt.delete()


class PutCollegeService(Service):
    def process(self):
        college_put = self.data                                    #data received from views
        clg = college_put.get('data')
        pk = clg.get('id')

        clg_put = College.objects.get(pk=pk)
        clg_name = clg.get('college_name')
        clg_city = clg.get('city')
        clg_state = clg.get('state')

        clg_put.college_name = clg_name
        clg_put.city = clg_city
        clg_put.state = clg_state
        clg_put.save()
        return clg_put



class CreateStudentService(Service):
    def process(self):
        student = self.data
        post_student = student.get('student_data')
        student_obj = Student.objects.create(
            first_name=post_student.get('first_name'),
            last_name=post_student.get('last_name'),
            branch=post_student.get('branch'),
            dob=post_student.get('dob')
        )
        return student_obj


class GetStudentService(Service):
    def process(self):
        std = self.data
        pk = std.get('pk')
        if pk:
            student_get = Student.objects.get(id=pk)
        else:
            student_get = Student.objects.all()
        return student_get


class DeleteStudentService(Service):
    def process(self):
        pk = self.data.get('pk')
        student_dlt = Student.objects.get(pk=pk)
        student_dlt.delete()


class PutStudentService(Service):
    def process(self):
        student_put = self.data
        student = student_put.get('data')
        pk = student.get('id')

        std_put = Student.objects.get(pk=pk)
        first_name = student.get('first_name')
        last_name = student.get('last_name')
        branch = student.get('branch')
        dob = student.get('dob')

        std_put.first_name = first_name
        std_put.last_name = last_name
        std_put.branch = branch
        std_put.dob = dob
        std_put.save()
        return std_put










