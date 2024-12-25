
import sqlite3

conn = sqlite3.connect("videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL
            )
''')

def list_all_videos():
    cursor.execute("SELECT * from videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,duration) VALUES (?, ?)", (name,time))
    conn.commit()

def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name = ? , duration = ? WHERE id = ?", (name,time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

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
            
    conn.close()
        
if __name__ == "__main__":
    main()
