# Base image
FROM python:3.10.12

# Set working directory in the container
WORKDIR /app

# Copy the required files into the container
COPY best_models /app/best_models
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Install necessary dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "--server.port=8501", "app.py"]
