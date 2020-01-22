from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')

class RegisterForm(FlaskForm):
   username = StringField('Имя пользователя', validators=[DataRequired()])
   email = StringField('Почта', validators=[DataRequired()])
   role = StringField('Кто ты по жизни', validators=[DataRequired()])
   password1 = PasswordField('Пароль', validators=[DataRequired()])
   password2 = PasswordField('Повторите Пароль', validators=[DataRequired()])
   submit = SubmitField('Регистрация')
   position = StringField('Должность', validators=[])
   department_number = StringField('№ Кафедры', validators=[])
   rank = StringField('Звание', validators=[])
   record_num = StringField('№ Зачетки', validators=[])
   group_num = StringField('№ Группы', validators=[])

class AddWorkForm(FlaskForm):
  title = StringField('Название работы', validators=[DataRequired()])
  theme = StringField('Тема', validators=[DataRequired()])
  conference = StringField('Название конференции', validators=[DataRequired()])
  conference_number = StringField('Номер конференции', validators=[DataRequired()])
  submit = SubmitField('Добавить научную работу')

class AddConferenceForm(FlaskForm):
  title = StringField('Название Конференции', validators=[DataRequired()]) 
  number = StringField('Номер Конференции', validators=[DataRequired()])
  theme = StringField('Тема Конференции', validators=[DataRequired()])
  date = StringField('Дата Проведения', validators=[DataRequired()])
  submit = SubmitField('Добавить Конференцию')

class Works(FlaskForm):
  submit = SubmitField('Пук Пук')
  names = StringField()

class IndexForm(FlaskForm):
  group = StringField('Номер группы')
  submit = SubmitField('Добавить группу')
  grant = StringField('Степуха')
  s_num = IntegerField('Зачетка')
  submit_s = SubmitField('Пык-Пык')