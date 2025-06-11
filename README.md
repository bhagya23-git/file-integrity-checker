#File-integrity-checker

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: BHAGYASHREEMA PANDA

*INTERN ID*: CT04DN04

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## Internship Task-1: File Integrity Checker – Description
In today's digital world, ensuring the **security and integrity of files** is a major concern, especially in the field of cybersecurity. As part of my internship in the **cybersecurity domain**, I was assigned Task-1, which involved designing and implementing a **File Integrity Checker using Python**. This project serves as a foundational cybersecurity utility that checks whether a file has been **tampered with, altered, or corrupted** since it was last verified.
### Objective and Functionality
The core objective of this task is to create a tool that can:
**Generate a hash value** (SHA-256) for any given file
**Store that hash securely**
**Compare the current hash** of the file with the stored one to detect any unauthorized changes
This ensures that users can verify the authenticity of a file over time. If even a single byte of the file is changed, the hash will be different — signaling a possible modification or security breach.
### Real-World Use Cases
The File Integrity Checker has a wide range of applications across industries:
1. **Cybersecurity & Malware Detection**: This tool is extremely useful for detecting unauthorized changes to system files or sensitive documents, which may indicate malware infections or cyber-attacks.
2. **Data Forensics**: In digital forensics, hash verification is used to ensure evidence files have not been altered during investigation. This tool can be a simplified version of how real-world forensic tools work.
3. **Software Development**: Software developers often provide hash values for their installers or updates. Users can use tools like this to **verify downloads** and ensure no one has injected malicious code.
4. **Backup Verification**: In IT environments where backups are frequently made, this tool can help verify that backups are identical to the originals and have not been corrupted.
5. **Document Integrity in Enterprises**: Businesses dealing with legal or sensitive documents can use this tool to detect unauthorized modifications to contracts, reports, or confidential files.
### Tools and Technologies Used
For implementing this project, the primary tool used is:
### Python Programming Language
Python was chosen due to its readability, ease of implementation, and robust standard libraries. Specifically:
* hashlib:
  * A built-in Python module that supports multiple hashing algorithms such as SHA-1, SHA-256, and MD5.
  * SHA-256 was used in this task due to its strong security and wide industry usage.
* File handling in Python:
  * Used to **open files in binary mode**, read content in chunks, and write or read stored hash files (like 'example.txt.hash').
* Optional logging feature:
  * Additional implementation can log events in a '.txt' file to record time-stamped integrity check results.
### Key Features
**Dynamic File Selection**: The user can input any file path at runtime, allowing the same script to work with multiple files.
**SHA-256 Hash Calculation**: Ensures a unique and secure digital fingerprint of the file.
**Integrity Comparison**: Alerts the user if the file has been modified since the last check.
**User Feedback**: Clearly informs the user if the file is “intact” or “has been modified.”
**Reusability and Simplicity**: Written in a way that even beginners in cybersecurity can understand and use it effectively.

#OUTPUT: 

![Image](https://github.com/user-attachments/assets/76d2dfb0-860a-4378-903b-88a297a2b13c)

