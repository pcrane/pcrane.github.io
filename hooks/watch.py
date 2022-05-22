#!/usr/bin/env python3
import json
import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from jinja2 import Environment, FileSystemLoader


class DummyHTTPHandler(BaseHTTPRequestHandler):
  logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s - %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')

  def do_GET(self):

    current_working_directory = os.getcwd()
    logging.info(current_working_directory)
    if self.path == "/":
      logging.info('rendering')

      template_directory = os.path.abspath(current_working_directory)
      env = Environment(
        loader=FileSystemLoader(template_directory)
      )
      template = env.get_template("template.html", template_directory)

      cv_file = os.path.join(current_working_directory, "cv.json")
      try:
        with open(cv_file, "r", encoding="utf-8") as cv:
          data = json.load(cv)
      except json.decoder.JSONDecodeError as e:
        self.send_response(500)
        self.end_headers()
        self.wfile.write("JSON Decoding Error".encode("utf-8"))
        logging.error("JSON Decoding Error", e)
        return

      self.send_response(200)
      self.end_headers()
      self.wfile.write(template.render(data).encode('utf-8'))
      return

    resource_path = str(self.path[1:])
    resource = os.path.join(current_working_directory, resource_path)
    try:
      with open(resource, 'rb') as f:
        self.send_response(200)
        self.end_headers()
        byte = f.read(4096)
        while byte != b"":
          self.wfile.write(byte)
          byte = f.read(4096)

    except FileNotFoundError:
      self.send_response(404)
      self.end_headers()


if __name__ == '__main__':
  import argparse

  # Command line argument handling:
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-a', '--address', help='default: 127.0.0.1')
  parser.add_argument('-p', '--port', help='default: 8080', type=int)
  args = parser.parse_args()

  template = 'template.html'
  content = 'cv.json'

  server = HTTPServer(
    (args.address or '127.0.0.1', args.port or 8080),
    lambda request, client_address, server: DummyHTTPHandler(request, client_address, server),
  )

  server.serve_forever()
