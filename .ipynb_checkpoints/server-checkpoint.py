{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "17ee4c94-a0ca-4414-b551-9a38b143b44e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\oktay\\anaconda3\\lib\\site-packages (3.0.3)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from flask) (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from flask) (1.6.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\oktay\\anaconda3\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.3)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "707315fc-d22a-450c-b668-5d86f0873341",
   "metadata": {},
   "outputs": [],
   "source": [
    "# server.py\n",
    "\n",
    "from flask import Flask, jsonify\n",
    "import os\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/greet', methods=['GET'])\n",
    "def greet():\n",
    "    return jsonify({\"message\": \"Merhaba Oktay!\"})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    port = int(os.environ.get(\"PORT\", 5000))  # Render PORT kullanımı\n",
    "    app.run(host='0.0.0.0', port=port)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a35a7351-29e2-4b70-9fa4-619022d09ca4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
