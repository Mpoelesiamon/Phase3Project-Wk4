import click
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from models import Teacher, Class, Student, session

@click.command()
@click.option('--action', prompt='Select action', type=click.Choice(['add_teacher','add_class','add_student']))
@click.pass_context
def main(ctx, action):
    if action == 'add_teacher':
        add_teacher(ctx)
    elif action == 'add_class':    
        add_class(ctx)
    elif action == 'add_student':
        add_student(ctx)
    else:
        print('provide valid options.')         

def add_teacher(ctx):
    name = click.prompt('Enter Teachers name')

    added= Teacher(name= name)
    session.add(added)
    session.commit()
    click.echo("\nEntered successifully")

def add_class(ctx):
    classname = click.prompt('Enter classname: ')
    # teacherid = click.prompt('Enter Teacher id: ')

    added= Class(class_name = classname, teacher_id= 1)
    session.add(added)
    session.commit()
    click.echo("\nEntered successifully")

    

def add_student(ctx):
    name = click.prompt('\nEnter studentname')

if __name__ == '__main__':
    main()