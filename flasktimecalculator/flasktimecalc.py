from flask import Flask, render_template, request

app = Flask(__name__)

def timecalc(current_time, future_time):
    def calc(current_hour, current_minute, current_period, future_hour, future_minute, future_period):
        if current_period == future_period and future_hour == 12 and current_hour != 12:
            hours_left = 24 - current_hour
        elif current_period == future_period and future_hour == current_hour and current_minute > future_minute:
            hours_left = 23
        elif current_period == future_period and current_hour == 12 and future_hour != 12:
            hours_left = future_hour
        elif current_period == future_period and current_hour == 12 and future_hour == 12 and future_minute < current_minute:
            hours_left = 24
        elif current_period == future_period and future_hour > current_hour:
            hours_left = future_hour - current_hour
        elif current_period == future_period and current_hour > future_hour:
            hours_left = future_hour + 24 - current_hour
        elif current_period != future_period:
            hours_left = 12 - current_hour + future_hour
        elif current_hour == future_hour and current_period == future_period:
            hours_left = 0

            
        if future_minute >= current_minute:
            minutes_left = future_minute - current_minute
        elif current_period == future_period and future_hour == current_hour and current_minute > future_minute:
            hours_left = 23
            minutes_left = 60 - (current_minute-future_minute)
        elif future_minute < current_minute:
            hours_left -= 1
            minutes_left = 60 - current_minute + future_minute
            timecalculated = str(hours_left) + " hours and " + str(minutes_left) + " minutes remain"
        return timecalculated
    # Defining current time variables
    splittime = current_time.split(":")
    current_hour = int(splittime[0])
    current_minute, current_period = splittime[1].split()
    current_minute = int(current_minute)

    # Defining future time variables
    splittime_future = future_time.split(":")
    future_hour = int(splittime_future[0])
    future_minute, future_period = splittime_future[1].split()
    future_minute = int(future_minute)
        
    return calc(current_hour, current_minute, current_period, future_hour, future_minute, future_period)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        current_time = request.form['current_time']
        future_time = request.form['future_time']
        
        try:
            result = timecalc(current_time, future_time)
        except ValueError:
            # Handle ValueError (invalid input)
            result = "Invalid input format. Please use HH:MM AM/PM."
        
        return render_template('home.html', result=result)

        
    return render_template('home.html')

@app.route("/results")
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)