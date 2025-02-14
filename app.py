from flask import Flask, render_template, request
from stories import generate_story, CATEGORY_OPTIONS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        category = request.form.get('category')
        # If only category is submitted (first step), show the options page.
        if category and not any(request.form.get(f'option{i}') for i in range(1, 7)):
            options_data = CATEGORY_OPTIONS.get(category, {})
            return render_template('index.html', category=category, options_data=options_data)
        
        # If category and all 6 options have been submitted, generate the story.
        if not category:
            return render_template('index.html', error_message="Please select a category.")
            
        options = [request.form.get(f'option{i}') for i in range(1, 7)]
        if None in options:
            options_data = CATEGORY_OPTIONS.get(category, {})
            return render_template('index.html', category=category, options_data=options_data, error_message="Please select all options.")
        
        story = generate_story(category, *options)
        return render_template('story.html', story=story)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)