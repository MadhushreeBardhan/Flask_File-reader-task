from flask import Flask, request, Response
import os

app = Flask(__name__)


@app.route('/')
@app.route('/<file_path>/', methods=['GET'])
def file_reader_view(file_path=None):
    params = request.args
    if file_path is not None:
        start_number = request.args.get('start')
        end_number = request.args.get('end')
        if params and start_number and end_number:
            started = False
            collected_lines = []
            with open(os.path.abspath(f"files/{file_path}"), "rb") as fp:
                for i, line in enumerate(fp.readlines()):
                    if i == int(start_number):
                        started = True
                        continue
                    if started and i == int(end_number):
                        break
                    if started == True:
                        collected_lines.append(line)
            return Response(collected_lines)
        else:
            f = open(os.path.abspath(f"files/{file_path}"), "rb")
            return Response(f.read(), mimetype='text/plain')

    else:
        f = open(os.path.abspath("files/file1.txt"), "rb")  # should give static path
        return Response(f.read(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True)
