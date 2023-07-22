from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_location_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}?token=5ba42ec046f3ae"
    response = requests.get(url)
    data = response.json()
    return data.get('country'), data.get('region')

@app.route('/')
def index():
    user_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    country, state = get_location_info(user_ip)
    
    return render_template('index.html', 
                           user_ip=user_ip,
                           country=country,
                           state=state)

if __name__ == '__main__':
    app.run()
