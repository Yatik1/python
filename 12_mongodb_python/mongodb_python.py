import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://yatiksrivastava1:jn1WjawKoUoV4d5Y@python-database.zaa1n.mongodb.net/?retryWrites=true&w=majority&appName=Python-database" ,tlsAllowInvalidCertificates=True)

db = client["videosmanager"]
collection = db["vedios"]

def list_all_videos():
    for video in collection.find():
        print(f"ID : {video['_id']} , Name : {video['name']} , Duration : {video['duration']}")

def add_video(name,time):
    collection.insert_one({"name":name,"duration":time})

def update_video(video_id, new_name, new_time):
    collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "duration": new_time}})

def delete_video(video_id):
    collection.delete_one({"_id": ObjectId(video_id)})

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