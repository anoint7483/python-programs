# Create a new presentation object
prs = Presentation()

# Function to add a slide with title and bullet points, with specific font sizes
def add_custom_slide(prs, title, content, bullet_points=None):
    slide_layout = prs.slide_layouts[1]  # Use the title and content layout
    slide = prs.slides.add_slide(slide_layout)
    title_shape = slide.shapes.title
    body_shape = slide.placeholders[1]

    # Set title
    title_shape.text = title
    title_shape.text_frame.paragraphs[0].font.size = Pt(42)
    title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)
    title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT

    # Add content
    tf = body_shape.text_frame
    tf.text = content
    tf.paragraphs[0].font.size = Pt(20)
    tf.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)
    tf.paragraphs[0].alignment = PP_ALIGN.LEFT

    # Add bullet points
    if bullet_points:
        for point in bullet_points:
            p = tf.add_paragraph()
            p.text = point
            p.level = 0
            p.font.size = Pt(20)
            p.font.color.rgb = RGBColor(0, 0, 0)
            p.alignment = PP_ALIGN.LEFT

# Add slides with custom font sizes
add_custom_slide(prs, "The 7 C's of Communication", "Mastering Effective Communication\nPresented by: [Your Name]\nDate: [Today's Date]")

add_custom_slide(prs, "Introduction", "Overview:", [
    "Importance of effective communication",
    "Introduction to the 7 C's"
])

add_custom_slide(prs, "Clear", "Definition: Ensure your message is easy to understand.", [
    "Use simple language.",
    "Avoid jargon.",
    "Be specific and precise.",
    "Provide examples or analogies for clarity."
])

add_custom_slide(prs, "Concise", "Definition: Keep your message brief and to the point.", [
    "Eliminate unnecessary words.",
    "Stick to relevant information.",
    "Focus on the main message."
])

add_custom_slide(prs, "Concrete", "Definition: Make sure your message is solid and specific.", [
    "Provide details and facts.",
    "Use vivid and precise words.",
    "Avoid vague statements."
])

add_custom_slide(prs, "Correct", "Definition: Ensure your message is accurate and free of errors.", [
    "Check for grammatical errors.",
    "Use the correct level of language.",
    "Verify facts before communicating."
])

add_custom_slide(prs, "Coherent", "Definition: Your message should be logical and consistent.", [
    "Organize information logically.",
    "Make sure each point connects to the main topic.",
    "Use transitions for smooth flow."
])

add_custom_slide(prs, "Complete", "Definition: Provide all necessary information.", [
    "Answer all potential questions.",
    "Include any required action steps.",
    "Anticipate the audience's needs."
])

add_custom_slide(prs, "Courteous", "Definition: Be polite and respectful.", [
    "Use a friendly tone.",
    "Show respect for the recipient.",
    "Be empathetic and considerate."
])

add_custom_slide(prs, "Conclusion", "Summary:", [
    "Recap of the 7 C's: Clear, Concise, Concrete, Correct, Coherent, Complete, Courteous.",
    "Importance of incorporating these principles in communication.",
    "Effective communication is key to success in both personal and professional settings. By mastering the 7 C's, you can enhance your communication skills and achieve better outcomes."
])

add_custom_slide(prs, "Questions & Answers", "Do you have any questions or need further clarification on the 7 C's of communication?")

# Save the custom presentation
custom_pptx_path = "/mnt/data/7_Cs_of_Communication_Presentation_Custom.pptx"
prs.save(custom_pptx_path)

custom_pptx_path
