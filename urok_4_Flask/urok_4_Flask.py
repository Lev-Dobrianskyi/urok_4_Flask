from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.json.ensure_ascii = False

me = {
    'name': 'Lev',
    'age': 15,
    'city': 'Ivano-Frankivsk',
    'skills': ['Python', 'JavaScript', 'Flask', 'HTML/CSS', 'SQL', 'C++', 'C#']
}

projects = [ #то нічого якщо я не додав спаравжні проекти?
    {
        'id': 1,
        'name': 'Веб-сайт для портфоліо',
        'description': 'Персональний веб-сайт з портфоліо проєктів та контактною інформацією'
    },
    {
        'id': 2,
        'name': 'Чат-бот на Python',
        'description': 'Простий чат-бот з використанням бібліотеки nlp для обробки природної мови'
    },
    {
        'id': 3,
        'name': 'API для управління списком завдань',
        'description': 'RESTful API для створення, читання та видалення завдань, розроблений на Flask'
    },
    {
        'id': 4,
        'name': 'Мобільний додаток для вивчення англійської',
        'description': 'Додаток для вивчення англійської мови з ігровими елементами та відслідженням прогресу'
    }
]

@app.route('/')
def index():
    return render_template('index.html', person=me, title='Головна')

@app.route('/about')
def about():
    return render_template('about.html', person=me, title='Про мене')

@app.route('/skills')
def skills():
    return render_template('skills.html', person=me, title='Навички')

@app.route('/project/<int:id>')
def project(id):
    for proj in projects:
        if proj['id'] == id:
            return render_template('project.html', project=proj, title=proj['name'])
    return 'Проєкт не знайдено', 404

@app.route('/api/me')
def api_me():
    return jsonify(me)

if __name__ == '__main__':
    app.run(debug=True)
