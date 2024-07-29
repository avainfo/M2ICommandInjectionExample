from flask import Flask, request, render_template_string
import os

app = Flask(__name__)


@app.route('/')
def index():
	return render_template_string('''
		<!doctype html>
		<html lang="en">
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
			<title>Command Injection Example</title>
		</head>
		<body>
			<div class="container">
				<h1>Ping a Host</h1>
				<form method="post" action="/ping">
					<div class="form-group">
						<label for="host">Host</label>
						<input type="text" class="form-control" id="host" name="host" placeholder="Enter host">
					</div>
					<button type="submit" class="btn btn-primary">Ping</button>
				</form>
				{% if result %}
				<h2>Result</h2>
				<pre>{{ result }}</pre>
				{% endif %}
			</div>
		</body>
		</html>
	''')


@app.route('/ping', methods=['POST'])
def ping():
	host = request.form['host']
	result = os.popen(f"ping {host}").read()
	return render_template_string('''
		<!doctype html>
		<html lang="en">
			<head>
				<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
				<title>Command Injection Example</title>
			</head>
			<body>
				<div class="container">
					<h1>Ping a Host</h1>
					<form method="post" action="/ping">
						<div class="form-group">
							<label for="host">Host</label>
							<input type="text" class="form-control" id="host" name="host" placeholder="Enter host">
						</div>
						<button type="submit" class="btn btn-primary">Ping</button>
					</form>
					<h2>Result</h2>
					<pre>{{ result }}</pre>
				</div>
			</body>
		</html>
		''', result=result)


if __name__ == '__main__':
	app.run(debug=True)

# 127.0.0.1 | echo "Faille trouvée !"