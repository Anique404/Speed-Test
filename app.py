from flask import Flask, render_template, jsonify
import speedtest


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/speedtest', methods=['GET'])
def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    # Measure download and upload speeds in Mbps
    download_speed_mbps = st.download() / 1_000_000  # Convert to Mbps
    upload_speed_mbps = st.upload() / 1_000_000      # Convert to Mbps

    # Convert to Kbps
    download_speed_kbps = download_speed_mbps * 1000
    upload_speed_kbps = upload_speed_mbps * 1000

    # Measure latency
    latency = st.results.ping  # Get the ping from the results

    return jsonify({
        'download_mbps': download_speed_mbps,
        'download_kbps': download_speed_kbps,
        'upload_mbps': upload_speed_mbps,
        'upload_kbps': upload_speed_kbps,
        'latency_unloaded': round(latency, 2),
        'latency_loaded': round(latency, 2),
        'ping': round(latency, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
