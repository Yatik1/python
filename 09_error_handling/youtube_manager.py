
def load_data():
    pass

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = load_data()
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
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")
        
if __name__ == "__main__":
    main()


