bl_info = {
    "name": "Toggle MMB Rotate",
    "category": "3D View",
    "author": "Robert Norenberg",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
}

import bpy

class ToggleMMBRotate(bpy.types.Operator):
    """Toggles rotation with middle mouse button"""
    bl_idname = "view3d.toggle_mmb_rotate"
    bl_label = "Toggle MMB Rotate"

    def execute(self, context):
        kmitems = bpy.context.window_manager.keyconfigs.active.keymaps["3D View"].keymap_items
        is_default = kmitems["view3d.rotate"].shift == False
        kmitems["view3d.rotate"].shift = is_default
        kmitems["view3d.move"].shift = not is_default

        self.report({'INFO'}, "mmb rotate off" if is_default else "mmb rotate on")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(ToggleMMBRotate)

def unregister():
    bpy.utils.unregister_class(ToggleMMBRotate)

if __name__ == "__main__":
    register()
