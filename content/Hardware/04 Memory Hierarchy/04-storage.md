# Storage: the permanent layer

**Learning objective:** after this section, a beginner should be able to explain what storage is, why it is slower than RAM, and why it is still essential.

## 1. Why this matters

RAM is fast but temporary. If everything lived only in RAM, all your files would disappear when you turn off the computer. Storage is the layer that keeps everything permanently — and understanding its speed matters for programs that read and write large files.

## 2. Explanation

**Storage** (SSD or hard disk) is the slowest and largest layer of memory. It is:

- **Very large** — terabytes.
- **Slow** — much slower than RAM (especially hard disks; SSDs are faster but still slower than RAM).
- **Permanent** — data stays when the power goes off.

Storage holds everything that must survive a reboot: the operating system, your programs, your files, your photos, your videos.

The trade-off is the same as before: storage is huge because it is slow and cheap. RAM is fast because it is small and expensive.

When a program needs data from storage, it is **loaded into RAM first**, then used by the CPU through cache and registers. That is why opening a large file can take a moment: the data has to travel from disk to RAM.

## 3. Diagram

<img width="1774" height="887" alt="微信图片_20261024132959_2476_8" src="https://github.com/user-attachments/assets/1cbacce4-5bba-42a7-bb4f-be97aa827ca2" />


## 4. Example

You open a 1 GB video file.

- The file sits on **storage** (disk/SSD).
- The video player loads chunks into **RAM**.
- The CPU decodes frames using **cache** and **registers**.
- The picture goes to the screen.

The first moment may feel slow — that is the disk → RAM transfer. After that, playback is smooth because the data is already in RAM.

## 5. Check yourself

1. What does storage hold?
2. Why is storage slower than RAM?
3. Why is storage still essential even though it is slow?
4. What happens when a program needs data from storage?
5. Order these by speed, fastest first: storage, RAM, cache, registers.

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on memory hierarchy.
