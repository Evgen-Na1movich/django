from django.shortcuts import render

from school.models import Group, Student


def all_groups_view(request):
    data_dict_with_groups = Group.objects.all()
    return render(request, 'groups.html', context={'groups': data_dict_with_groups, 'title' : 'Главная страница'})


def all_students_of_the_groups(request, group_id):
    group = Group.objects.get(id=group_id)
    groups_students = Student.objects.filter(group_id=group_id)
    return render(request, 'students.html', context={'students': groups_students, 'group': group,
                                                     'title': f"Студенты группы {group.name}"})
