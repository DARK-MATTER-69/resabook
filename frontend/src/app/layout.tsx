import { AuthProvider } from "@/context/AuthContext";
// ... autres imports existants (police, globals.css, etc. — garde-les)

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="fr">
      <body>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}