import sqlite3


conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

# Remember:

# cursor.execute() → Executes SQL queries.

# conn.commit() → Saves changes.

# conn.rollback() → Undoes uncommitted changes.

# conn.close() → Closes the connection.

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        duration TEXT NOT NULL
    )
 ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("\nNo videos found.")
        return
    else:
        for video in videos:
            print(video)

def add_video(title, duration):
    cursor.execute("INSERT INTO videos (title, duration) VALUES (?, ?)", (title, duration))
    conn.commit()
    print(f"Video '{title}' added successfully.")

def update_video(video_id, new_title, new_duration):
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()

    if video is None:
        print(f"No video found with ID {video_id}.")
        return
    new_title = new_title if new_title else video[1]
    new_duration = new_duration if new_duration else video[2]
    cursor.execute("UPDATE videos SET title = ?, duration = ? WHERE id = ?", (new_title, new_duration, video_id))
    
    conn.commit()
    print(f"Video with ID {video_id} updated successfully.")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print(f"No video found with ID {video_id}.")
    else:
        print(f"Video with ID {video_id} deleted successfully.")


def main():
    while True:
        try:
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
                    add_video(title, duration)
                case "3":
                    list_videos()
                    video_id = int(input("Enter video ID to update: "))
                    title = input("Enter new video title (leave blank to keep current): ")
                    duration = input("Enter new video duration (leave blank to keep current): ")
                    update_video(video_id, title, duration)
                case "4":
                    list_videos()
                    video_id = int(input("Enter video ID to delete: "))
                    delete_video(video_id)
                case "5":
                    print("Exiting YouTube Manager. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid ID! Please enter a numeric video ID.")

    conn.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting YouTube Manager. Goodbye!")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()
        print("Database connection closed.")