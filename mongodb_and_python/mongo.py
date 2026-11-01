
import pymongo
from bson.objectid import ObjectId


def connect_to_mongo():
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://learnpy:learnpy@cluster0.qb2l9h3.mongodb.net/",
            tlsAllowInvalidCertificates=True
        )

        # Check connection
        client.admin.command("ping")

        db = client["youtube_videos_db"]
        return db

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None


# Connect to database
db = connect_to_mongo()

if db is not None:
    videos_collection = db["videos"]
else:
    videos_collection = None


# 1. List all videos
def list_videos():
    if videos_collection is None:
        print("Database not connected!")
        return

    videos = videos_collection.find()

    print("\n--- YouTube Videos ---")

    found = False

    for index, video in enumerate(videos, start=1):
        found = True
        print(f"ID: {index}")
        print(f"MongoDB ID: {video['_id']}")
        print(f"Title: {video['name']}")
        print(f"Duration: {video['time']}")
        print("----------------------")

    if not found:
        print("No videos found.")


# 2. Add a video
def add_video(title, duration):
    if videos_collection is None:
        print("Database not connected!")
        return

    video = {
        "name": title,
        "time": duration
    }

    result = videos_collection.insert_one(video)

    print(f"Video added successfully! ID: {result.inserted_id}")


# 3. Update a video
def update_video(video_id, new_title, new_duration):
    if videos_collection is None:
        print("Database not connected!")
        return

    try:
        # Find video by its MongoDB ID
        video = videos_collection.find_one({
            "_id": ObjectId(video_id)
        })

        if video is None:
            print("Video not found!")
            return

        updated_data = {}

        if new_title.strip():
            updated_data["name"] = new_title

        if new_duration.strip():
            updated_data["time"] = new_duration

        if not updated_data:
            print("No changes made.")
            return

        videos_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": updated_data}
        )

        print("Video updated successfully!")

    except Exception:
        print("Invalid MongoDB ID!")


# 4. Delete a video
def delete_video(video_id):
    if videos_collection is None:
        print("Database not connected!")
        return

    try:
        result = videos_collection.delete_one({
            "_id": ObjectId(video_id)
        })

        if result.deleted_count > 0:
            print("Video deleted successfully!")
        else:
            print("Video not found!")

    except Exception:
        print("Invalid MongoDB ID!")


# Main menu
def main():
    while True:
        print("\nYouTube Manager Menu:")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                list_videos()

            case "2":
                title = input("Enter video title: ")
                duration = input("Enter video duration: ")

                if title.strip() and duration.strip():
                    add_video(title, duration)
                else:
                    print("Title and duration cannot be empty!")

            case "3":
                try:
                    list_videos()

                    video_id = input(
                        "Enter MongoDB video ID to update: "
                    )

                    new_title = input(
                        "Enter new title (leave blank to keep current): "
                    )

                    new_duration = input(
                        "Enter new duration (leave blank to keep current): "
                    )

                    update_video(
                        video_id,
                        new_title,
                        new_duration
                    )

                except ValueError:
                    print("Invalid ID!")

            case "4":
                list_videos()

                video_id = input(
                    "Enter MongoDB video ID to delete: "
                )

                delete_video(video_id)

            case "5":
                print("Exiting the YouTube Manager. Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()
