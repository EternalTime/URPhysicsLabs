\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{physlab}[2026/04/20 Physics Lab Class]

% Pass options to exam class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{exam}}
\ProcessOptions\relax
\LoadClass{exam}

% Geometry setup
\RequirePackage{geometry}
\geometry{
	paper=letterpaper,
	margin=1in,
}

% Colors
\RequirePackage[table,dvipsnames]{xcolor}

% Table packages
\RequirePackage{multirow}
\RequirePackage{multicol}
\RequirePackage{makecell}

% Font and encoding
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage[english]{babel}
\RequirePackage{mathpazo}

% Math packages
\RequirePackage{amsmath, amsfonts, amsthm, amssymb}
\RequirePackage{braket, nicefrac}
\RequirePackage{dsfont}

% Lists and columns
\RequirePackage{enumitem, multicol}

% Checklist environment for equipment
\newlist{todolist}{itemize}{2}
\setlist[todolist]{label=$\square$}

% Graphics and floats
\RequirePackage{graphicx, float, wrapfig}
\RequirePackage{keystroke}
\RequirePackage[font=footnotesize, textfont=sl]{caption}
\RequirePackage{sidecap}
\RequirePackage{tikz}
\RequirePackage{circuitikz}
\RequirePackage{csquotes}
\RequirePackage{ulem}

% Hyperlinks
\RequirePackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue, bookmarks=true, breaklinks=true]{hyperref}

% Graphics path and bibliography
\graphicspath{{graphics/}{./}}
\RequirePackage[style=ieee]{biblatex}

% SI units
\RequirePackage{siunitx}
\DeclareSIUnit{\nothing}{\relax}

% Chemical formulas
\RequirePackage[version=4]{mhchem}

% Caption types for postlab exercises
\DeclareCaptionType{graph}
\DeclareCaptionType{data table}

% Custom commands
\newcommand{\source}[1]{\caption*{Source: {#1}}}
\labelformat{equation}{(#1)}
\def\equationautorefname#1{}
\newcommand{\bs}[1]{\boldsymbol{#1}}

% University colors: see https://brand.rochester.edu/visual-identity/color-system/
\definecolor{RocYellow}{RGB}{255,209,0}
\definecolor{RocBlue}{RGB}{0,59,113}
\definecolor{EverButter}{RGB}{255,243,177}

% Lab metadata commands
\newcommand{\labtitle}[1]{\def\@labtitle{#1}}
\newcommand{\labnum}[1]{\def\@labnum{#1}}
\newcommand{\labnumroman}[1]{\def\@labnumroman{#1}}
\newcommand{\course}[1]{\def\@course{#1}}
\newcommand{\coursesubtitle}[1]{\def\@coursesubtitle{#1}}

% Default values
\def\@labtitle{TITLE}
\def\@labnum{1}
\def\@labnumroman{I}
\def\@course{PHYSICS 141}
\def\@coursesubtitle{Honors Mechanics}

% Title page
\renewcommand{\maketitle}{
	\begin{titlepage}
		\centering
        \includegraphics[width=0.8\textwidth]{UofRlogo.png}\par\vspace{3cm}\vspace{4.5cm}
		{\huge\bfseries Laboratory \@labnumroman \par}
        {\LARGE\bfseries \@labtitle \par}
        \vfill
		{\scshape\LARGE Department of Physics \& Astronomy\par}
		\vspace{0.3cm}
		{\scshape\Large \@course\par \@coursesubtitle\par}
		\vspace{1cm}
		{\large \@date\par}
	\end{titlepage}
}

% Section formatting
\RequirePackage{titlesec}
\titleformat{\section}{\large\bfseries\color{RocBlue}}{\thesection.}{0.5em}{}
\titleformat{\subsection}{\normalsize\bfseries\color{RocBlue}}{\thesubsection.}{0.5em}{}

% Lab section environments
\newenvironment{objective}
{\section*{Objective}\begin{quote}\itshape}
{\end{quote}}

\newenvironment{equipment}
{\section*{Equipment}\begin{itemize}[nosep]}
{\end{itemize}}

\newenvironment{procedure}
{\section*{Procedure}\begin{enumerate}}
{\end{enumerate}}

\newenvironment{introduction}
{\section*{Introduction}}
{}

\newenvironment{theory}
{\section*{Theory}}
{}

\newenvironment{experiment}
{\section*{Experiment}}
{}

\newenvironment{analysis}
{\section*{Data Analysis}}
{}

\newenvironment{conclusion}
{\section*{Conclusion}\begin{quote}}
{\end{quote}}

% Student info header (used in prelab and postlab)
\newcommand{\studentheader}{
	\begin{flushleft}
	\textbf{Name:} \underline{\hspace{8.25cm}} \hfill \textbf{Date:} \underline{\hspace{6cm}}\\[0.8em]
	\textbf{Collaborators:} \underline{\hspace{7.25cm}} \hfill \textbf{Lab Section:} \underline{\hspace{3.5cm}}
	\end{flushleft}\vspace{-10pt}
}

% Prelab section
\newenvironment{prelab}{
	\newpage
    \pagestyle{headandfoot}
    \firstpageheadrule
    \runningheadrule
    \firstpageheader{Laboratory \@labnumroman}{\@labtitle}{PRELAB}
    \runningheader{Laboratory \@labnumroman}{\@labtitle}{PRELAB}
    \firstpagefooter{University of Rochester}{}{\thepage}
    \runningfooter{University of Rochester}{}{\thepage}
	\studentheader
	\vspace{-5pt}
	\fullwidth{\section*{\textsc{Prelab Exercises} (\pointsinrange{prelab} points)}}\vspace{-1em}
    \noindent\textsl{This prelab must be completed and handed in to the lab TA at the start of the lab.}\\[0em]
    \begin{questions}
    \begingradingrange{prelab}
}{
    \endgradingrange{prelab}
    \newcounter{nprelab}
    \setcounter{nprelab}{\value{question}}
    \end{questions}
    \newpage
}

% Postlab section
\newenvironment{postlab}{
	\newpage
    \pagestyle{headandfoot}
    \firstpageheadrule
    \runningheadrule
    \firstpageheader{Laboratory \@labnumroman}{\@labtitle}{POSTLAB}
    \runningheader{Laboratory \@labnumroman}{\@labtitle}{POSTLAB}
    \firstpagefooter{University of Rochester}{}{\thepage}
    \runningfooter{University of Rochester}{}{\thepage}
	\studentheader
	\vspace{-0.3cm}
	\fullwidth{\section*{\textsc{Postlab Exercises} (\pointsinrange{postlab} points)}}\vspace{-1em}
    \noindent\textsl{Submit the postlab to the TA at the end of the lab.}\\[0em]
    \begin{questions}
    \addtocounter{question}{\value{nprelab}}
    \begingradingrange{postlab}
}{
    \endgradingrange{postlab}
    \end{questions}
    \newpage
}

% Lab section (default page style)
\newenvironment{labsection}{
	\newpage
	\pagestyle{plain}
}{}

% Photon style for tikz diagrams
\usetikzlibrary{decorations.markings,decorations.pathmorphing}
\tikzset{
    photon/.style={
        -{Latex[length=5,width=4]},
        YellowOrange,
        line width=0.8,
        decorate,
        decoration={snake, amplitude=1.0, segment length=5, post length=5}
    }
}

% Question format
\qformat{{\bf Question \thequestion}\hfill{\sl\bf \totalpoints{} \points}\vrule depth 1em width 0pt}
