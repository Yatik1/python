
import sqlite3

conn = sqlite3.connect("videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS video (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL,
            )
''')

def list_all_videos():
    pass

def add_video(name,time):
    pass

def update_video(video_id,name,time):
    pass

def delete_video(video_id):
    pass

def main():
    while True:
        print("-" *70)
        print(f" {' ' * 25 } VIDEO MANAGER")
        print("-" *70 , "\n")

        print("Choose the following choice: ")
        print("1. List all the video you want to watch")
        print("2. Add a video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit the app")

        choice = input("Enter your choice : ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                name=input("Enter name of video : ")
                time=input("Enter time duration of the video : ")
                add_video(name,time)
            case "3":
                video_id = input('Enter video id you wish to update : ')
                name=input("Enter updated name of video : ")
                time=input("Enter updated time duration of the video : ")
                update_video(video_id,name,time)
            case "4":
                video_id = input('Enter video id you wish to delete : ')
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid Choice")
        
if __name__ == "__main__":
    main()
