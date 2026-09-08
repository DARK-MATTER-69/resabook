export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen grid grid-cols-1 md:grid-cols-2">
      <div className="flex items-center justify-center p-8">
        <div className="w-full max-w-[420px]">{children}</div>
      </div>
      <div className="hidden md:flex bg-primary items-center justify-center p-12">
        <div className="text-primary-foreground max-w-md text-center space-y-4">
          <h2 className="text-3xl font-bold">ResaBook</h2>
          <p className="text-lg opacity-90">
            Réservez vos prestations en 30 secondes.
          </p>
        </div>
      </div>
    </div>
  );
}