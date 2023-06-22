class BeforeSavePlugin:
    def before_save_document(self, *args, **kwargs):
        print(f"BeforeSavePlugin: before_save, data: {args}, {kwargs}")
