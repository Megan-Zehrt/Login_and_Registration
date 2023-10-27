from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'secret'
DATABASE = "login_and_register_schema"