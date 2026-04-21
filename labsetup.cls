%% labsetup.cls — University of Rochester Physics Lab Setup Sheet
%% Usage: \documentclass{labsetup}
%%
%% Required preamble commands:
%%   \labnumber{3}
%%   \labtitle{Projectile Motion}
%%
%% Document body commands:
%%   \setupphoto{filename}          — full-width completed-setup photo
%%   \equipitem{name}{location}{filename}  — one equipment entry with checkbox

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{labsetup}[2026/04/20 UR Physics Lab Setup Sheet]

%% ── Base class ────────────────────────────────────────────────────────────────
\LoadClass[11pt, letterpaper]{article}

%% ── Packages ──────────────────────────────────────────────────────────────────
\RequirePackage[margin=1in, top=0.75in]{geometry}
\RequirePackage{graphicx}
\graphicspath{{Lab Equipment/}}
\RequirePackage{xcolor}
\RequirePackage{tabularx}
\RequirePackage{booktabs}
\RequirePackage{enumitem}
\RequirePackage{array}
\RequirePackage{calc}
\RequirePackage{fancyhdr}
\RequirePackage{fontenc}          % T1 encoding
\RequirePackage{lmodern}
\RequirePackage{tikz}             % for the UR header rule
\RequirePackage{amssymb}          % \Square for checkbox
\RequirePackage{microtype}
\RequirePackage{caption}
\captionsetup{labelformat=empty, skip=4pt}

%% ── UR Brand Colors ───────────────────────────────────────────────────────────
\definecolor{URblue}{RGB}{0, 45, 98}      % UR official blue
\definecolor{URgold}{RGB}{255, 184, 28}   % UR official gold

%% ── Metadata storage ─────────────────────────────────────────────────────────
\newcommand{\@labnumber}{}
\newcommand{\@labtitle}{}
\newcommand{\labnumber}[1]{\renewcommand{\@labnumber}{#1}}
\newcommand{\labtitle}[1]{\renewcommand{\@labtitle}{#1}}

%% ── Page style ────────────────────────────────────────────────────────────────
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}

% Header: UR blue band across full width
\fancyhead[L]{%
  \begin{tikzpicture}[remember picture, overlay]
    \fill[URblue] (-1in, 0.1in) rectangle (\textwidth + 1in, 0.55in);
    \fill[URgold] (-1in, 0.08in) rectangle (\textwidth + 1in, 0.1in);
  \end{tikzpicture}%
  \hspace{0pt}%
  \raisebox{0.15in}{%
    \color{white}\sffamily\bfseries\large
    University of Rochester \quad\textbar\quad
    Lab~\@labnumber: \@labtitle
  }%
}

\fancyfoot[C]{\small\sffamily\color{gray}\thepage}

%% ── \setupphoto ───────────────────────────────────────────────────────────────
%% Prints a full-width photo with a "Completed Setup" caption below it.
\newcommand{\setupphoto}[1]{%
  \vspace{0.5em}
  \begin{center}
    \includegraphics[width=\textwidth, keepaspectratio]{#1}
    \captionof{figure}{\sffamily\bfseries Completed Setup}
  \end{center}
  \vspace{0.5em}
  \hrule height 1pt \relax
  \vspace{1em}
}

%% ── \equipitem ────────────────────────────────────────────────────────────────
%% Arguments: {Equipment Name}{Storage Location}{Photo filename}
%% Produces a row with:
%%   [ checkbox ]  Name / Location  |  photo thumbnail
\newlength{\@photowidth}
\setlength{\@photowidth}{0.34\textwidth}

\newcommand{\equipitem}[3]{%
  \noindent
  \begin{tabular}{@{}p{0.04\textwidth} p{0.54\textwidth} p{\@photowidth}@{}}
    % checkbox column
    \raisebox{0.3em}{\Large$\square$} &
    % name + location column
    \begin{minipage}[t]{0.60\textwidth}
      \vspace{0pt}
      {\sffamily\bfseries #1}\\[2pt]
      {\sffamily\small\color{gray}Storage: #2}
    \end{minipage} &
    % photo column
    \begin{minipage}[t]{\@photowidth}
      \vspace{0pt}
      \includegraphics[width=\@photowidth, height=0.18\textheight,
                       keepaspectratio]{#3}
    \end{minipage}
  \end{tabular}%
  \par\vspace{0.6em}
  \hrule height 0.4pt
  \vspace{0.6em}
}

%% ── Section heading shortcut ─────────────────────────────────────────────────
\renewcommand{\section}[1]{%
  \vspace{0.8em}
  {\sffamily\bfseries\large\color{URblue} #1}
  \vspace{0.3em}
  \hrule height 1.5pt \relax
  \vspace{0.5em}
}

\endinput
