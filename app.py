from flask import Flask, render_template, request

app = Flask(__name__)

# Data kurs USD ke IDR dan USD ke EUR dari 2014 hingga 2024
usd_to_idr = {
    "2014": "12,440",
    "2015": "14,700",
    "2016": "13,900",
    "2017": "13,300",
    "2018": "14,500",
    "2019": "14,000",
    "2020": "15,000",
    "2021": "14,500",
    "2022": "15,700",
    "2023": "15,425",
    "2024": "15,500",
}

usd_to_eur = {
    "2014": "0.83",
    "2015": "0.95",
    "2016": "0.96",
    "2017": "0.85",
    "2018": "0.88",
    "2019": "0.90",
    "2020": "0.82",
    "2021": "0.85",
    "2022": "0.96",
    "2023": "0.92",
    "2024": "0.91",
}

usd_to_yen = {
    "2014": "120",
    "2015": "125",
    "2016": "115",
    "2017": "114",
    "2018": "114",
    "2019": "112",
    "2020": "110",
    "2021": "115",
    "2022": "151",
    "2023": "145",
    "2024": "150",
}

@app.route('/', methods=['GET', 'POST'])
def home():
    
    currency_filter = request.form.get('currency_filter')  # Get selected currency filter
    selected_years = request.form.getlist('years')  # Get selected years as a list
    filtered_results = {}

    if selected_years:
        # Pilih kurs berdasarkan pilihan pengguna (IDR atau EUR)
        if currency_filter == 'USD to IDR':
            for year in selected_years:
                filtered_results[year] = usd_to_idr.get(year)
        if currency_filter == 'USD to EUR':
            for year in selected_years:
                filtered_results[year] = usd_to_eur.get(year)
        elif currency_filter == 'USD to YEN':
            for year in selected_years:
                filtered_results[year] = usd_to_yen.get(year)

    return render_template('index.html', 
                           exchange_rates=usd_to_idr, 
                           selected_years=selected_years, 
                           filtered_results=filtered_results, 
                           currency_filter=currency_filter)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)