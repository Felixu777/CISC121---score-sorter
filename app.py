import gradio as gr

# Bubble Sort Algorithm (simple for CISC-121)
def bubble_sort(arr, ascending):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                # Sort from LOW to HIGH
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                # Sort from HIGH to LOW
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Main function
def sort_scores(input_text, order):
    try:
        # Convert input into numbers
        scores = [float(s.strip()) for s in input_text.split(",")]
        
        # Choose order
        ascending = (order == "Low to High")
        sorted_list = bubble_sort(scores, ascending)
        
        return f"Sorted scores: {sorted_list}"
    
    except:
        return "ERROR! Use commas to separate numbers. Example: 85,92,76"

# Create web UI
with gr.Blocks() as demo:
    gr.Markdown("# 📚 Student Score Sorting Tool")
    gr.Markdown("Enter scores separated by commas")
    
    input_box = gr.Textbox(label="Enter Scores")
    order = gr.Radio(["Low to High", "High to Low"], label="Sort Order", value="High to Low")
    btn = gr.Button("Sort Scores")
    output = gr.Textbox(label="Result")
    
    # 👇 FIXED HERE
    btn.click(fn=sort_scores, inputs=[input_box, order], outputs=output)

# Run the app
if __name__ == "__main__":
    demo.launch()