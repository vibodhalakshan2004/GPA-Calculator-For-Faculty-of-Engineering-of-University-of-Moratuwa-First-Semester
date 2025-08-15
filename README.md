# 🎓 UoM Engineering Faculty – GPA Calculator (Semester 1)

A simple **Tkinter** app to compute GPA for the **University of Moratuwa – Faculty of Engineering (First Semester)**.  
Features a clean `ttk.Style()` UI and weighted credit calculation.

---

## ✨ Features
- Dropdown grade selection for each Semester 1 subject
- **Weighted GPA** using official credit values (total = 14)
- Modern look via `ttk.Style()` (no external libraries)

---

## 📚 Subjects & Credits (Semester 1)
| Code   | Subject (short) | Credits |
|-------:|------------------|--------:|
| MA1014 | Mathematics      | 3 |
| CS1033 | Computing        | 3 |
| EE1014 | Electrical Eng.  | 2 |
| CE1023 | Civil Eng.       | 2 |
| ME1033 | Mechanical Eng.  | 2 |
| MT1023 | Materials Eng.   | 2 |

**Total credits:** `14`

> If your department/semester uses different credits, edit the `credits` list in `gpa_calculator.py`.

---

## 🧮 Grade → Point Mapping
| Grade | Points |
|:-----:|:------:|
| A+, A | 4.0 |
| A-    | 3.7 |
| B+    | 3.3 |
| B     | 3.0 |
| B-    | 2.7 |
| C+    | 2.3 |
| C     | 2.0 |
| C-    | 1.7 |
| D     | 1.0 |
| F     | 0.0 |

**GPA formula:**  
\[
\text{GPA} = \frac{\sum (\text{grade points} \times \text{credits})}{\sum \text{credits}}
\]
For the default subjects, \(\sum \text{credits} = 14\).

---

## ▶️ Run Locally
**Requirements:** Python 3 (Tkinter ships with Python on Windows/macOS/Linux)

```bash
python gpa_calculator.py
