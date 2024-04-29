import re

def clean_html(raw_html):
    """Remove HTML tags from the given string."""
    cleanr = re.compile('<.*?>')  # Regular expression to match HTML tags
    cleantext = re.sub(cleanr, '', raw_html)  # Replace HTML tags with empty string
    return cleantext

def print_formatted_directions(directions):
    """Print directions with improved formatting."""
    for step in directions:
        # Remove HTML tags
        step = clean_html(step)
        
        # Optionally, add further formatting enhancements here
        # For example, replace 'Turn right' with '➡️ Turn right', etc.
        step = step.replace('Turn right', '➡️ Turn right')
        step = step.replace('Turn left', '⬅️ Turn left')
        step = step.replace('Continue', '➡️ Continue')
        step = step.replace('Head', '🔼 Head')
        step = step.replace('At the roundabout, take the', '🔄 At the roundabout, take the')
        
        print(step)


