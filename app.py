from flask import Flask, render_template, request, redirect
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain, pending=blockchain.pending_transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = request.form['amount']
    blockchain.add_transaction(sender, receiver, amount)
    return redirect('/')

@app.route('/mine_block')
def mine_block():
    blockchain.mine_block()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
