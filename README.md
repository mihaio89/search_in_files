The situation where the "Modified" timestamp is earlier than the "Created" timestamp can happen for a few reasons, depending on your operating system and specific file operations:

### 1. **File Copying or Moving**:
   - When you **copy** a file, the "Created" timestamp on the new file reflects the time of the copy, not the original file's creation time.
   - The "Modified" timestamp, however, is carried over from the original file. If the original file was last modified before the time of the copy, the "Modified" timestamp will be earlier than the "Created" timestamp.

   For example, if you copied a file to a new location or even a different folder, the "Created" timestamp would show the time of the copy, but the "Modified" time would remain the same as when the file was last changed.

### 2. **Backup and Restore Operations**:
   - Some backup or restore tools restore files with their original modification times, but the creation time reflects when the file was restored to the system.

### 3. **Operating System Differences**:
   - Some operating systems handle timestamps differently. For example:
     - **Windows** keeps both creation and modification times.
     - **Linux/macOS** may not track file creation time natively, so the creation time may reflect when the file was added to the current filesystem (e.g., after a move or copy).

### 4. **File System Specifics**:
   - Some file systems (like FAT32) don't track creation time, and certain operations may cause the creation timestamp to be newer than the modification timestamp.

### Summary:
The reason you're seeing "Modified" as earlier than "Created" is likely due to file copying, moving, or restoring, where the system sets the new "Created" timestamp, but retains the original "Modified" timestamp from when the file was last changed.