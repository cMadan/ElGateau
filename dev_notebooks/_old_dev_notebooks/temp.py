        # define on_click event handler
        def on_click(event):
            """
            Capture the x,y-coordinates of a mouse click 
            on the display_state in mpl.
            """ 
            ix, iy = event.xdata, event.ydata
            # x,y pixel coordinates for click
            click_xy = [ix, iy]
            # re-code to (r,c) of click
            r = int(np.floor(click_xy[1]/80))+1
            c = int(np.floor(click_xy[0]/80))+1
            key = (r, c)
            # convert from (r,c) to 1-15
            key = self.key_remap(key)
            # convert to device notation, then back to intuitive 1-15
            key = self.key_remap(key)
            # update key_state with this key press
            self.key_state.append(key)

        # connect mpl figure and on_click event handler
        cid = self.fig.canvas.mpl_connect('button_press_event', on_click)