def clamp_rgb_value(value):
  return max(0, min(255, value))

def convert_negative_rgb_values(red, green, blue):
  positive_red = red if red >= 0 else 256 + red
  positive_green = green if green >= 0 else 256 + green
  positive_blue = blue if blue >= 0 else 256 + blue
  return clamp_rgb_value(positive_red), clamp_rgb_value(positive_green), clamp_rgb_value(positive_blue)

red = 30
green = -22
blue = -27

converted_red, converted_green, converted_blue = convert_negative_rgb_values(red, green, blue)

print(converted_red)  # prints 156
print(converted_green)  # prints 205
print(converted_blue)  # prints 230





