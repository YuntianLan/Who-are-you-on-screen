from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.helpers import Matcher
import numpy as np

project_name = "Who are you on screen?"
net_id = ""

matcher = Matcher()

@irsystem.route('/', methods=['GET'])
def search():
	# print(request.args)
	if not request.args.get('questionOne'):
		return render_template('search.html', \
			name = project_name, netid = net_id)

	query = [
		int(request.args.get('questionOne')),
		int(request.args.get('questionTwo')),
		int(request.args.get('questionThree')),
		int(request.args.get('questionFour')),
		int(request.args.get('questionFive')),
		int(request.args.get('questionSix')),
		int(request.args.get('questionSeven')),
		int(request.args.get('questionEight')),
		int(request.args.get('questionNine')),
		int(request.args.get('questionTen')),
	]
	cnames, mnames, quotes, vecs, user_vec = matcher.match(query)

	return render_template('result.html', \
		char1 = cnames[0], movie1 = mnames[0], quote1 = quotes[0],\
		vec1 = vecs[0], user_vec = user_vec)



