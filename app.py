{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "05ed9a79-da33-4e8d-9790-4ebe3170a6f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-01 22:07:40.350 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\rahul\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-01 22:07:40.350 Session state does not function when running a script without `streamlit run`\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "# Load model\n",
    "model = joblib.load(r'E:\\Data_science\\project\\Supervised ML Project\\best_model.pkl')\n",
    "\n",
    "st.title(\"Insurance Charges Prediction\")\n",
    "\n",
    "age = st.number_input(\"Age\", 18, 100, 30)\n",
    "sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "bmi = st.number_input(\"BMI\", 10.0, 50.0, 25.0)\n",
    "children = st.slider(\"Number of Children\", 0, 5, 0)\n",
    "smoker = st.selectbox(\"Smoker\", [\"yes\", \"no\"])\n",
    "region = st.selectbox(\"Region\", [\"northeast\", \"northwest\", \"southeast\", \"southwest\"])\n",
    "\n",
    "data = {\n",
    "    \"age\": age,\n",
    "    \"bmi\": bmi,\n",
    "    \"children\": children,\n",
    "    \"sex_male\": 1 if sex == \"male\" else 0,\n",
    "    \"smoker_yes\": 1 if smoker == \"yes\" else 0,\n",
    "    \"region_northwest\": 1 if region == \"northwest\" else 0,\n",
    "    \"region_southeast\": 1 if region == \"southeast\" else 0,\n",
    "    \"region_southwest\": 1 if region == \"southwest\" else 0\n",
    "}\n",
    "input_df = pd.DataFrame([data])\n",
    "log_pred = model.predict(input_df)[0]\n",
    "predicted_charge = np.expm1(log_pred)\n",
    "\n",
    "st.subheader(f\"Predicted Insurance Charge: ${predicted_charge:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48ce90fa-8f1e-433c-80fd-84a6776e63b8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
