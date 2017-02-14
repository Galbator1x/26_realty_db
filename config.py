import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_URL = os.environ.get('DATABASE_URL',
            'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CITIES = [
            ('Бабаевский район', 'Бабаево'),
            ('Бабушкинский район', 'Село имени Бабушкина'),
            ('Белозерский район', 'Белозерск'),
            ('Великоустюгский район', 'Великий Устюг'),
            ('Верховажский район', 'Верховажье'),
            ('Вожегодский район', 'Вожега'),
            ('Вологодский район', 'Вологда'),
            ('Вытегорский район', 'Вытегра'),
            ('Грязовецкий район', 'Грязовец'),
            ('Кадуйский район', 'Кадуй'),
            ('Кирилловский район', 'Кириллов'),
            ('Кичменгско-Городецкий район', 'Кичменгский Городок'),
            ('Вашкинский район', 'Липин Бор'),
            ('Никольский район', 'Никольск'),
            ('Нюксенский район', 'Нюксеница'),
            ('Сокольский район', 'Сокол'),
            ('Сямженский район', 'Сямжа'),
            ('Тарногский район', 'Тарногский Городок'),
            ('Тотемский район', 'Тотьма'),
            ('Усть-Кубинский район', 'Устье'),
            ('Устюженский район', 'Устюжна'),
            ('Харовский район', 'Харовск'),
            ('Чагодощенский район', 'Чагода'),
            ('Череповецкий район', 'Череповец'),
            ('Шекснинский район', 'Шексна'),
            ('Междуреченский район', 'Шуйское')
            ]


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
