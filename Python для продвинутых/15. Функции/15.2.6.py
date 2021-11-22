def info_kwargs(**kwargs):
    for key in sorted(kwargs):
        print(f'{key}: {kwargs[key]}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
