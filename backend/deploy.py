import os
import shutil
import zipfile
import subprocess

# Préparation
def main():
    # le travail commence
    print("Creating Lambda deployment package...")

    # Clean up : on supprime l’ancien dossier on supprime l’ancien ZIP et on repart proprement
    if os.path.exists("lambda-package"):
        shutil.rmtree("lambda-package")
    if os.path.exists("lambda-deployment.zip"):
        os.remove("lambda-deployment.zip")

    # Création du dossier de travail
    # Ce dossier va contenir: le ton code les bibliothèques Python et les données (data/)
    os.makedirs("lambda-package")

    # nstallation des dépendances (PARTIE LA PLUS IMPORTANTE)/////
    print("Installing dependencies for Lambda runtime...")

    # Use the official AWS Lambda Python 3.12 image
    # This ensures compatibility with Lambda's runtime environment
    # “Installe toutes les bibliothèques de requirements.txt comme si tu étais AWS Lambda et mets-les dans lambda-package/
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{os.getcwd()}:/var/task",
            "--platform",
            "linux/amd64",  # Force x86_64 architecture
            "--entrypoint",
            "",  # Override the default entrypoint
            "public.ecr.aws/lambda/python:3.12",
            "/bin/sh",
            "-c",
            "pip install --target /var/task/lambda-package -r /var/task/requirements.txt --platform manylinux2014_x86_64 --only-binary=:all: --upgrade",
        ],
        check=True,
    )

    # Copy du code
    print("Copying application files...")
    for file in ["server.py", "lambda_handler.py", "context.py", "resources.py"]:
        if os.path.exists(file):
            shutil.copy2(file, "lambda-package/")
    
    # Copy des données
    if os.path.exists("data"):
        shutil.copytree("data", "lambda-package/data")

    # Create zip LE fichier que tu enverras à AWS Lambda.
    print("Creating zip file...")
    with zipfile.ZipFile("lambda-deployment.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("lambda-package"):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, "lambda-package")
                zipf.write(file_path, arcname)

    # Show package size
    size_mb = os.path.getsize("lambda-deployment.zip") / (1024 * 1024)
    print(f"✓ Created lambda-deployment.zip ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()