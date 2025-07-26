#include <iostream>
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include "miko_typography_wrapper.hpp"
#include "miko_layout.hpp"
#include "miko_layout_wrapper.hpp"
#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QGroupBox>
#include <QMessageBox>
#include <QFrame>

class MikoWindow : public QWidget {
Q_OBJECT

public:
    MikoWindow(QWidget *parent = nullptr) : QWidget(parent) {
        setupUI();
        connectSignals();
        setWindowTitle("MikoCSS Qt6 Demo Application");
        setMinimumSize(800, 600);
        
        // Apply window background - changed to dark gray
        auto bg_color = miko::get_color("gray-800");
        setStyleSheet(QString("QWidget { background-color: rgb(%1, %2, %3); }")
                     .arg(static_cast<int>(bg_color.r * 255)).arg(static_cast<int>(bg_color.g * 255)).arg(static_cast<int>(bg_color.b * 255)));
    }

private slots:
    void onPrimaryButtonClicked() {
        QMessageBox::information(this, "MikoCSS", "Primary button clicked!");
    }
    
    void onSecondaryButtonClicked() {
        QMessageBox::information(this, "MikoCSS", "Secondary button clicked!");
    }
    
    void onDangerButtonClicked() {
        QMessageBox::warning(this, "MikoCSS", "Danger button clicked!");
    }
    
    void onSuccessButtonClicked() {
        QMessageBox::information(this, "MikoCSS", "Success! Operation completed.");
    }

private:
    void setupUI() {
        auto mainLayout = new QVBoxLayout(this);
        mainLayout->setSpacing(20);
        mainLayout->setContentsMargins(30, 30, 30, 30);
        
        // Header section
        createHeaderSection(mainLayout);
        
        // Button showcase section
        createButtonSection(mainLayout);
        
        // Input section
        createInputSection(mainLayout);
        
        // Text display section
        createTextSection(mainLayout);
    }
    
    void createHeaderSection(QVBoxLayout* mainLayout) {
        auto headerFrame = new QFrame();
        auto headerLayout = new QVBoxLayout(headerFrame);
        
        // Main title
        auto titleLabel = new QLabel("MikoCSS Qt6 Demo");
        auto title_color = miko::get_color("blue-600");
        auto title_size = miko::get_text_size("xl");
        auto title_weight = miko::get_font_weight("bold");
        
        titleLabel->setStyleSheet(QString(
            "color: rgb(%1, %2, %3); "
            "font-size: %4px; "
            "font-weight: %5; "
            "margin-bottom: 10px;"
        ).arg(static_cast<int>(title_color.r * 255)).arg(static_cast<int>(title_color.g * 255)).arg(static_cast<int>(title_color.b * 255))
         .arg(title_size.font_size_px).arg(title_weight.weight));
        titleLabel->setAlignment(Qt::AlignCenter);
        
        // Subtitle
        auto subtitleLabel = new QLabel("Showcasing MikoCSS styling system integration");
        auto subtitle_color = miko::get_color("gray-600");
        auto subtitle_size = miko::get_text_size("base");
        
        subtitleLabel->setStyleSheet(QString(
            "color: rgb(%1, %2, %3); "
            "font-size: %4px;"
        ).arg(static_cast<int>(subtitle_color.r * 255)).arg(static_cast<int>(subtitle_color.g * 255)).arg(static_cast<int>(subtitle_color.b * 255))
         .arg(subtitle_size.font_size_px));
        subtitleLabel->setAlignment(Qt::AlignCenter);
        
        headerLayout->addWidget(titleLabel);
        headerLayout->addWidget(subtitleLabel);
        
        // Style the header frame
        auto frame_bg = miko::get_color("white");
        headerFrame->setStyleSheet(QString(
            "QFrame { "
            "background-color: rgb(%1, %2, %3); "
            "border-radius: 12px; "
            "padding: 20px; "
            "border: 1px solid rgb(229, 231, 235); "
            "}"
        ).arg(static_cast<int>(frame_bg.r * 255)).arg(static_cast<int>(frame_bg.g * 255)).arg(static_cast<int>(frame_bg.b * 255)));
        
        mainLayout->addWidget(headerFrame);
    }
    
    void createButtonSection(QVBoxLayout* mainLayout) {
        auto buttonGroup = new QGroupBox("Interactive Buttons");
        auto buttonLayout = new QGridLayout(buttonGroup);
        buttonLayout->setSpacing(15);
        
        // Primary button
        primaryBtn = new QPushButton("Primary Action");
        styleButton(primaryBtn, "blue-500", "white", "hover:blue-600");
        
        // Secondary button
        secondaryBtn = new QPushButton("Secondary Action");
        styleButton(secondaryBtn, "gray-500", "white", "hover:gray-600");
        
        // Success button
        successBtn = new QPushButton("Success Action");
        styleButton(successBtn, "green-500", "white", "hover:green-600");
        
        // Danger button
        dangerBtn = new QPushButton("Danger Action");
        styleButton(dangerBtn, "red-500", "white", "hover:red-600");
        
        // Warning button
        auto warningBtn = new QPushButton("Warning Action");
        styleButton(warningBtn, "yellow-500", "gray-900", "hover:yellow-600");
        
        // Info button
        auto infoBtn = new QPushButton("Info Action");
        styleButton(infoBtn, "cyan-500", "white", "hover:cyan-600");
        
        buttonLayout->addWidget(primaryBtn, 0, 0);
        buttonLayout->addWidget(secondaryBtn, 0, 1);
        buttonLayout->addWidget(successBtn, 1, 0);
        buttonLayout->addWidget(dangerBtn, 1, 1);
        buttonLayout->addWidget(warningBtn, 2, 0);
        buttonLayout->addWidget(infoBtn, 2, 1);
        
        mainLayout->addWidget(buttonGroup);
    }
    
    void createInputSection(QVBoxLayout* mainLayout) {
        auto inputGroup = new QGroupBox("Input Fields");
        auto inputLayout = new QVBoxLayout(inputGroup);
        
        // Text input
        auto textInput = new QLineEdit();
        textInput->setPlaceholderText("Enter your text here...");
        styleInput(textInput);
        
        // Email input
        auto emailInput = new QLineEdit();
        emailInput->setPlaceholderText("Enter your email...");
        styleInput(emailInput);
        
        inputLayout->addWidget(new QLabel("Text Input:"));
        inputLayout->addWidget(textInput);
        inputLayout->addWidget(new QLabel("Email Input:"));
        inputLayout->addWidget(emailInput);
        
        mainLayout->addWidget(inputGroup);
    }
    
    void createTextSection(QVBoxLayout* mainLayout) {
        auto textGroup = new QGroupBox("Text Display");
        auto textLayout = new QVBoxLayout(textGroup);
        
        // Rich text area
        auto textArea = new QTextEdit();
        textArea->setMaximumHeight(150);
        textArea->setPlainText(
            "This is a demonstration of MikoCSS integration with Qt6. "
            "The styling system provides consistent colors, typography, and layout "
            "across different UI frameworks. You can see how MikoCSS colors and "
            "typography are applied to create a cohesive design system."
        );
        
        auto text_color = miko::get_color("gray-700");
        auto text_size = miko::get_text_size("sm");
        auto bg_color = miko::get_color("gray-50");
        
        textArea->setStyleSheet(QString(
            "QTextEdit { "
            "color: rgb(%1, %2, %3); "
            "font-size: %4px; "
            "background-color: rgb(%5, %6, %7); "
            "border: 1px solid rgb(209, 213, 219); "
            "border-radius: 6px; "
            "padding: 12px; "
            "}"
        ).arg(static_cast<int>(text_color.r * 255)).arg(static_cast<int>(text_color.g * 255)).arg(static_cast<int>(text_color.b * 255))
         .arg(text_size.font_size_px)
         .arg(static_cast<int>(bg_color.r * 255)).arg(static_cast<int>(bg_color.g * 255)).arg(static_cast<int>(bg_color.b * 255)));
        
        textLayout->addWidget(textArea);
        mainLayout->addWidget(textGroup);
    }
    
    void styleButton(QPushButton* button, const QString& bgColor, const QString& textColor, const QString& hoverColor) {
        // Add fallback colors in case the requested color doesn't exist
        auto bg = miko::get_color(bgColor.toStdString());
        auto text = miko::get_color(textColor.toStdString());
        
        // Fallback to basic colors if lookup fails
        if (bg.r == 0 && bg.g == 0 && bg.b == 0) {
            bg = miko::get_color("blue-500"); // fallback
        }
        if (text.r == 0 && text.g == 0 && text.b == 0) {
            text = miko::get_color("white"); // fallback  
        }
        
        auto btn_size = miko::get_text_size("base");
        auto btn_weight = miko::get_font_weight("medium");
        
        // Simplified hover color
        auto hover = miko::get_color("blue-600");
        
        button->setStyleSheet(QString(
            "QPushButton { "
            "background-color: rgb(%1, %2, %3); "
            "color: rgb(%4, %5, %6); "
            "font-size: %7px; "
            "font-weight: %8; "
            "border: 2px solid rgb(100, 100, 100); "  // Add visible border for debugging
            "border-radius: 8px; "
            "padding: 12px 24px; "
            "min-width: 120px; "
            "min-height: 40px; "  // Ensure minimum height
            "} "
            "QPushButton:hover { "
            "background-color: rgb(%9, %10, %11); "
            "} "
            "QPushButton:pressed { "
            "background-color: rgb(%12, %13, %14); "
            "}"
        ).arg(static_cast<int>(bg.r * 255)).arg(static_cast<int>(bg.g * 255)).arg(static_cast<int>(bg.b * 255))
         .arg(static_cast<int>(text.r * 255)).arg(static_cast<int>(text.g * 255)).arg(static_cast<int>(text.b * 255))
         .arg(btn_size.font_size_px).arg(btn_weight.weight)
         .arg(static_cast<int>(hover.r * 255)).arg(static_cast<int>(hover.g * 255)).arg(static_cast<int>(hover.b * 255))
         .arg(std::max(0, static_cast<int>(hover.r * 255) - 20)).arg(std::max(0, static_cast<int>(hover.g * 255) - 20)).arg(std::max(0, static_cast<int>(hover.b * 255) - 20)));
         
        // Debug: Ensure button is visible
        button->setVisible(true);
        button->show();
    } // <- This closing brace was missing!
    
    void styleInput(QLineEdit* input) {
        auto border_color = miko::get_color("gray-300");
        auto focus_color = miko::get_color("blue-500");
        auto text_color = miko::get_color("gray-900");
        auto bg_color = miko::get_color("white");
        auto text_size = miko::get_text_size("base");
        
        input->setStyleSheet(QString(
            "QLineEdit { "
            "background-color: rgb(%1, %2, %3); "
            "color: rgb(%4, %5, %6); "
            "font-size: %7px; "
            "border: 2px solid rgb(%8, %9, %10); "
            "border-radius: 6px; "
            "padding: 8px 12px; "
            "} "
            "QLineEdit:focus { "
            "border-color: rgb(%11, %12, %13); "
            "}"
        ).arg(static_cast<int>(bg_color.r * 255)).arg(static_cast<int>(bg_color.g * 255)).arg(static_cast<int>(bg_color.b * 255))
         .arg(static_cast<int>(text_color.r * 255)).arg(static_cast<int>(text_color.g * 255)).arg(static_cast<int>(text_color.b * 255))
         .arg(text_size.font_size_px)
         .arg(static_cast<int>(border_color.r * 255)).arg(static_cast<int>(border_color.g * 255)).arg(static_cast<int>(border_color.b * 255))
         .arg(static_cast<int>(focus_color.r * 255)).arg(static_cast<int>(focus_color.g * 255)).arg(static_cast<int>(focus_color.b * 255)));
    }
    
    void connectSignals() {
        connect(primaryBtn, &QPushButton::clicked, this, &MikoWindow::onPrimaryButtonClicked);
        connect(secondaryBtn, &QPushButton::clicked, this, &MikoWindow::onSecondaryButtonClicked);
        connect(dangerBtn, &QPushButton::clicked, this, &MikoWindow::onDangerButtonClicked);
        connect(successBtn, &QPushButton::clicked, this, &MikoWindow::onSuccessButtonClicked);
    }
    
    QPushButton* primaryBtn;
    QPushButton* secondaryBtn;
    QPushButton* dangerBtn;
    QPushButton* successBtn;
};

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    
    MikoWindow window;
    window.show();
    
    return app.exec();
}

#include "main.moc"