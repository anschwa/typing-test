#!/usr/bin/env python

from livereload import Server, shell

server = Server()

style = ("style.scss", "style.css")
script = ("typing-test.js", "typing-test-compiled.js")

server.watch(style[0], shell(["sass", style[0]], output=style[1]))
server.watch(script[0], shell(["babel", script[0]], output=script[1]))
server.watch("index.html")

server.serve(port=8080, host="localhost", open_url=True)
