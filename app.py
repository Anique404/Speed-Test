from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-speed')
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps

        return render_template('result.html', download=download_speed, upload=upload_speed)
    except speedtest.SpeedtestBestServerFailure as e:
        return jsonify({"error": "Unable to connect to servers to test latency."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
