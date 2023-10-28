#include <stdio.h>
#include <gtk/gtk.h>

void runPythonProgram(GtkWidget *widget, gpointer data) {
    gchar *command = "python3 ";
    system(command);
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *notebook;
    GtkWidget *tabLabel;

    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    gtk_window_set_default_size(GTK_WINDOW(window), 800, 600);

    // Create a notebook (tab container)
    notebook = gtk_notebook_new();
    gtk_container_add(GTK_CONTAINER(window), notebook);

    // Create the "Main Program" tab
    tabLabel = gtk_label_new("Main Program");
    gtk_notebook_append_page(GTK_NOTEBOOK(notebook), gtk_label_new(""), tabLabel);

    // Create the "Info" tab
    tabLabel = gtk_label_new("Info");
    gtk_notebook_append_page(GTK_NOTEBOOK(notebook), gtk_label_new(""), tabLabel);

    // Create the "Help" tab
    tabLabel = gtk_label_new("Help");
    gtk_notebook_append_page(GTK_NOTEBOOK(notebook), gtk_label_new(""), tabLabel);

    // Create 6 additional tabs
    for (int i = 1; i <= 6; i++) {
        char tabName[20];
        snprintf(tabName, sizeof(tabName), "Tab %d", i);
        tabLabel = gtk_label_new(tabName);
        gtk_notebook_append_page(GTK_NOTEBOOK(notebook), gtk_label_new(""), tabLabel);
    }

    // Show all widgets
    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}
