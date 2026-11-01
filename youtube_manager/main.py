import json

def load_data():
    try:
        with open('youtube_videos.json', 'r') as file:
            # json.load() reads the JSON data from the file and converts it into a Python object (e.g., list or dictionary)
            return json.load(file)
    except FileNotFoundError:
        return []

#helper function to save data to a JSON file
def save_data(videos):
    with open('youtube_videos.json', 'w') as file:
        #json.dump() converts the Python object (e.g., list or dictionary) into a JSON formatted string and writes it to the file
        json.dump(videos, file)


def list_videos(videos):
    print("\n")
    print("*" * 70)
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video['title']} - Duration: {video['duration']}")
    print("*" * 70)

def add_video(videos):
    input_title = input("Enter video title: ")
    input_duration = input("Enter video duration: ")
    videos.append({"title": input_title, "duration": input_duration})
    save_data(videos)

def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the number of the video to update: ")) - 1
    if 0 <= index < len(videos):
        input_title = input("Enter new video title: ")
        input_duration = input("Enter new video duration: ")
        videos[index] = {"title": input_title, "duration": input_duration}
        save_data(videos)

def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the number of the video to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data(videos)
    else:
        print("Invalid index. No video deleted.")

def main():
    videos = load_data()  # Load existing videos from a data source (e.g., file, database)
    while True:
        print("\nYouTube Manager Menu:")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        # print(videos)

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()