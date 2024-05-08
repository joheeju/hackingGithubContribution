import subprocess


if __name__ == '__main__':
    for i in range(1, 400):
        with open("fakeContribution.txt", "a") as f:
            f.write("try ")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "--date", f"\"{i} day ago\"", "-m", "Fake commit"])
        subprocess.run(["git", "push"])
        print(f"Commit pushed {i}")
