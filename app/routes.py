from app import wealthApp, db, appPath
from app.forms import LoginForm, UploadPortfolio, AddNewStock
from app.models import User, Security
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug import secure_filename
import config 
import os



@wealthApp.route('/')
@wealthApp.route('/index')
@login_required
def index():
	user = {"username":"Manoj","networth":"1000 INR","networth_change":"100 INR"}
	return render_template('index.html', title='Home', user=user)

@login_required
@wealthApp.route('/upload')
def upload_file():
	#user = {"username":"Manoj","networth":"1000 INR","networth_change":"100 INR"}
	form = UploadPortfolio()
	return render_template('upload.html',title='Upload',form=form)


@login_required
@wealthApp.route('/<security_id>/edit', methods=['GET','POST'])
def edit_security(security_id):
	sec = Security.query.filter_by(id=security_id)
	quantity = form.quantity.data
	price = form.price.data

@login_required
@wealthApp.route('/uploader', methods=['GET','POST'])
def uploader():
	print("TestPrint !!")
	print(request.files['uploadedFile'])
	if request.method == 'POST':
		f = request.files['uploadedFile']
		#path = basedir.join(Config.PORTFOLIO_PATH)
		#filePath = os.path.join(basedir, Config.PORTFOLIO_PATH,'',f.filename)
		#print(filePath)
		#f.save(filePath)
		#f.save(secure_filename(f.filename))
		relative_path = os.path.join(wealthApp.config['UPLOAD_FOLDER'], secure_filename(f.filename))
		f.save(os.path.join(appPath , relative_path))

	return redirect(url_for('getStockList'))


@login_required
@wealthApp.route('/<security_id>/delete')
def delete_security(security_id):
	security = Security.query.filter_by(id=security_id).first()
	print(security)
	db.session.delete(security)
	db.session.commit()
	print("Deleted rercord")
	return redirect(url_for('getStockList'))

@wealthApp.route('/mystocks')
@login_required
def getStockList():
	#user = current_user
	#print(current_user)
	#print(current_user.username)
	#user = User.query.filter_by(username=current_user.username)
	##print()
	securities = Security.query.filter_by(user_id=current_user.id)
	#print(securities)
	return render_template('tables.html', title='Stocks', user=current_user, stocksdata=securities)

@wealthApp.route('/login', methods=['GET','POST'])
def login():
	print("Go to login page1")
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	print("Go to login page2")
	if form.validate_on_submit():
		print("Go to login page3")
		user = User.query.filter_by(username=form.username.data).first()
		print(user)
		print(form.password.data)
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	print("Go to login page4")
	return render_template('login.html', title="Sign In", form=form)


@login_required
@wealthApp.route('/addstock',methods=['GET','POST'])
def addstock():
	form = AddNewStock()
	print("OusSide validate form!")
	if form.validate_on_submit():
		print("Inside validate form!")
		#Security.query.filter_by(user_id=current_user.id)
		stockName = form.stockName.data
		buyPrice = form.buyPrice.data
		quantity = form.quantity.data
		#date = form.date.data

		s = Security(security_type='Stock',security_name=stockName, country='India',buy_price=buyPrice, currency='INR', units=quantity, user_id=current_user.id )
		db.session.add(s)
		db.session.commit()
		return redirect(url_for('getStockList'))
	return render_template('addStock.html',form=form)


@wealthApp.route('/logout')
def logout():
	print("logging out !!")
	logout_user()
	return redirect(url_for('index'))