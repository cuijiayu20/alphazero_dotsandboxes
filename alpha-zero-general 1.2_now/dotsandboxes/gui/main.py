import multiprocessing
import threading

from dotsandboxes.gui.global_var import edge_number
from dotsandboxes.gui.global_var import action_copy
import pygame

# 棋盘大小
class GUI:


    action =None
    def update(action):
        # Update the GUI according to the action
        # Get the edge number from the action
        GUI.action =action
        # Color the edge with the corresponding color


        # Update the display



    def create_board( board_size=5):

        # Initialize pygame
        pygame.init()

        # Define the dimensions of the board
        board_size = 5
        width, height = 800, 800
        piece_size = width // (board_size + 1)
        accept_new_input = True

        # Create the screen
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        # Fill the screen with a color
        screen.fill((255, 255, 255))  # Set the background to white

        # Calculate the offset to center the board
        offset = (width - piece_size * board_size) // 2
        #一个映射
        edge_mapping = GUI.create_edge_mapping(board_size, piece_size, offset)
        # Draw the edges
        for row in range(board_size + 1):  # There are board_size+1 vertical edges
            for col in range(board_size):  # There are board_size horizontal edges
                GUI.draw_vertical_edge(screen, (row * piece_size + offset, col * piece_size + offset), (0, 0, 0), piece_size)
        for row in range(board_size):  # There are board_size horizontal edges
            for col in range(board_size + 1):  # There are board_size+1 vertical edges
                GUI.draw_horizontal_edge(screen, (row * piece_size + offset, col * piece_size + offset), (0, 0, 0), piece_size)

        pygame.display.update()

        # Main loop
        running = True
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and accept_new_input:  # change this line
                    # 调用find_edge_number函数获取边的编号
                    edge_number.append(GUI.find_edge_number(event, edge_mapping, offset, piece_size, board_size))
                    accept_new_input = False  # Add this line
                    # 打印边的编号
                    if edge_number[-1] is not None:
                        print("Clicked edge number:", edge_number)
                        for e in edge_number:
                            GUI.color_edge(screen, edge_mapping, e, (0, 255, 0), board_size, piece_size)
                    if action_copy is not None:
                        for a in action_copy:
                            if a not in edge_number:
                                GUI.color_edge(screen, edge_mapping, a, (255, 0, 0), board_size, piece_size)
                        accept_new_input = True
                    else:
                        continue
                        #GUI.color_edge(screen, edge_mapping, GUI.edge_number[-1], (255, 0, 0), board_size, piece_size)# Color the first edge red

                        # from test import get_new_action
                        # action = get_new_action()
                        # GUI.color_edge(screen, edge_mapping, action, (0, 255, 0), board_size, piece_size)
        pygame.quit()


    def draw_horizontal_edge(screen, pos, color, size):
        pygame.draw.rect(screen, color, (pos[0], pos[1], size, size//10))

    def draw_vertical_edge(screen, pos, color, size):
        pygame.draw.rect(screen, color, (pos[0], pos[1], size//10, size))

    def create_edge_mapping(board_size, piece_size, offset):
        edge_mapping = {}

        # Map the horizontal edges
        edge_number = 0
        for row in range(board_size + 1):
            for col in range(board_size):
                edge_mapping[edge_number] = (col * piece_size + offset, row * piece_size + offset)
                edge_number += 1

        # No additional increment here to leave a gap

        # Map the vertical edges
        for col in range(board_size):
            for row in range(board_size+1):
                edge_mapping[edge_number] = (row * piece_size + offset, col * piece_size + offset)
                edge_number += 1

        return edge_mapping

    def color_edge(screen, edge_mapping, edge_number, color,board_size,piece_size):
        # Get the position of the edge
        try:
            # Get the position of the edge
            edge_pos = edge_mapping[edge_number]

            # Determine whether the edge is horizontal or vertical
            if edge_number < board_size * (board_size + 1):  # The edge is horizontal
                GUI.draw_horizontal_edge(screen, edge_pos, color, piece_size)
            elif edge_number == 30:
                GUI.draw_vertical_edge(screen, edge_pos, color, piece_size)
            else:  # The edge is vertical
                GUI.draw_vertical_edge(screen, edge_pos, color, piece_size)

            pygame.display.update()

        except KeyError:
            print("Edge number exceeds the limit, ignoring...")

    def find_edge_number(event, edge_mapping, offset, piece_size, board_size):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the click
            x, y = event.pos

            # Iterate over the edges
            for number, position in edge_mapping.items():
                edge_x, edge_y = position

                if number < board_size * (board_size +1):  # The edge is horizontal
                    # Check if the click is within the edge boundaries
                    if edge_x <= x <= edge_x + piece_size and edge_y <= y <= edge_y + piece_size // 10:

                        return number
                else:  # The edge is vertical
                    # Check if the click is within the edge boundaries
                    if edge_x <= x <= edge_x + piece_size // 10 and edge_y <= y <= edge_y + piece_size:
                        return number

        # Return None if it's not a mouse button down event or if the click is not on an edge
        return None

